import logging

logger = logging.getLogger(__name__)

def purchase_ticket(request):
    logger.debug("purchase_ticket view called")
    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            ticket_type = form.cleaned_data['ticket_type']
            quantity = form.cleaned_data['quantity']

            try:
                # Send email to customer
                send_mail(
                    'Thank you for your purchase',
                    f'Thank you for purchasing {quantity} ticket(s) for the event.',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )

                # Send email to client
                send_mail(
                    'New Ticket Purchase',
                    f'Name: {name}\nPhone Number: {phone_number}\nE-mail: {email}',
                    settings.DEFAULT_FROM_EMAIL,
                    ['info@networkinginheels.co.ke'],
                    fail_silently=False,
                )
            except Exception as e:
                logger.error(f"Error sending email: {e}")
                return render(request, 'tickets/purchase_ticket.html', {'form': form, 'error': str(e)})

            return redirect('ticket_success')
    else:
        form = TicketPurchaseForm()
    return render(request, 'tickets/purchase_ticket.html', {'form': form})

def ticket_success(request):
    return render(request, 'tickets/ticket_success.html')
