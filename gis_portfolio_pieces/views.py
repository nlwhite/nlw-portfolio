from django.shortcuts import render, get_object_or_404
from .models import PortItem
from .models import PortItemPiece
from gis_portfolio_pieces.forms import ContactForm

from django.shortcuts import redirect
from django.template.loader import get_template
from django.core.mail import send_mail

from django.contrib import messages

# Create your views here.
def nlw(request):
    pieces = PortItem.objects
    return render(request,'gis_portfolio_pieces/home.html', {'pieces': pieces})

def detail(request, piece_id):
    parent_piece = get_object_or_404(PortItem, pk=piece_id)
    piece_items = parent_piece.items.all
    return render(request, 'gis_portfolio_pieces/detail.html', {'piece_items':piece_items, 'piece_info':parent_piece})

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            messages.success(request, 'Message sent')
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the contact information
            template = get_template('gis_portfolio_pieces/contact_template.txt')
            context = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
            }

            content = template.render(context)

            send_mail('Contact Form Message', content + '\nSent from: ' + contact_email, 'web@nlw.io', ['nicoleleewhite@gmail.com'], fail_silently=False)


            return redirect('contact')


    return render(request, 'gis_portfolio_pieces/contact.html', {'form': form_class})
