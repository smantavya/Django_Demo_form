from django.shortcuts import render,reverse
from form.models import MyUser
from form.forms import NewUserForm, PaymentForm
from django.http import HttpResponseRedirect
from instamojo_wrapper import Instamojo


api = Instamojo(api_key = "test_0d558ff1b2e45eba8a6f135784b" ,
                        auth_token = "test_f6dbb7574a0b80225f71aef2c50",
                        endpoint='https://test.instamojo.com/api/1.1/')

# Create your views here.
def thankyou(request):
    form = PaymentForm(request.POST)
    if request.method == 'POST':
        print("\n\n"+str(request.POST))
        form = PaymentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            response = api.payment_request_create(
            amount = str(data['amount']),
            purpose = data['purpose'],
            send_email = False,
            send_sms = False,
            email = data['email'],
            buyer_name = data['name'],
            phone = data['contact_no'],
            redirect_url = "http://www.example.com/handle_redirect.py"
            )
            return HttpResponseRedirect(response['payment_request']['longurl'])
        else:
            form = PaymentForm()

    return render(request, 'thankyou.html', {'form' :form})

def users(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('thankyou'))
        else:
            print("FORM INVALID!")

    return render(request,'forms.html', {'form':form})
