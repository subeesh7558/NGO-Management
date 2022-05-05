from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from datetime import datetime
from django.contrib.auth import authenticate, login, logout

def index(request):
	return render(request, 'welfare_temp/index.html')

def about(request):
	return render(request, 'welfare_temp/about.html')

def causes(request):
    return render(request, 'welfare_temp/causes.html')

def donate(request):
    return render(request, 'welfare_temp/donate.html') 


def gallery(request):
    return render(request, 'welfare_temp/gallery.html')


def event(request):
    return render(request, 'welfare_temp/event.html')  

def contact(request):
    return render(request, 'welfare_temp/contact.html')

def donation(request):
    return render(request, 'welfare_temp/donation.html')

def reg(request):
    designations=designation.objects.all()

    return render(request, 'welfare_temp/reg.html',{'designations':designations})                                             


def  loginwelfare(request):
    return render(request, 'welfare_temp/loginwelfare.html')



def reg_rest(request):
    return render(request, 'welfare_temp/reg_rest.html')                                             


def loginrest(request):
    return render(request, 'welfare_temp/loginrest.html')



def ngo(request):
    return redirect('/ngo/')








def login(request):
    Donar = designation.objects.get(designation="Donar")
    Ngo = designation.objects.get(designation="Ngo")
    if request.method == 'POST':
        username  = request.POST['uname']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            request.session['SAdm_id'] = user.id
            return redirect( 'Admin_index')

        elif user_registration.objects.filter(username=request.POST['uname'], password=request.POST['password'],designation=Donar.id,status="approved").exists():
                
                member=user_registration.objects.get(username=request.POST['uname'], password=request.POST['password'])
                request.session['doid'] = member.designation_id
                request.session['usernamets1'] = member.username
                request.session['Tnr_id'] = member.id 
                mem=user_registration.objects.filter(id= member.id)
                
                return render(request,'admin_temp/Donar_index.html',{'mem':mem})

        elif user_registration.objects.filter(username=request.POST['uname'], password=request.POST['password'],designation=Ngo.id,status="approved").exists():
                
                member=user_registration.objects.get(username=request.POST['uname'], password=request.POST['password'])
                request.session['ngid'] = member.designation_id
                request.session['usernamets1'] = member.username
                request.session['Tne_id'] = member.id 
                mem1=user_registration.objects.filter(id= member.id)
                
                return render(request,'admin_temp/Ngo_index.html',{'mem1':mem1})

        elif restaurant_registration.objects.filter(username=request.POST['uname'], password=request.POST['password']).exists():
                member=restaurant_registration.objects.get(username=request.POST['uname'], password=request.POST['password'])
                request.session['uname'] = member.username
                request.session['re_id'] = member.id 
                mem3=restaurant_registration.objects.filter(id= member.id)
                
                return render(request,'admin_temp/Restaurant_index.html',{'mem3':mem3})

        else:
            context = {'msg_error': 'Invalid data'}
            return render(request, 'welfare_temp/loginwelfare.html', context)
    return render(request,'welfare_temp/loginwelfare.html')


def Registration(request):
    if request.method == 'POST':
        designations=designation.objects.all()
        acc = user_registration()
        acc.firstname = request.POST['fname']
        acc.lastname = request.POST['lname']
        acc.username = request.POST['uname']
        acc.dateofbirth = request.POST['dateofbirth']
        acc.gender = request.POST['gender']
        desi_id = request.POST['desig']
        acc.designation_id = desi_id
        acc.status = "pending"
        acc.email = request.POST['email']
        acc.password = request.POST['password']
        acc.mobile = request.POST['mobile']
        acc.alternativeno = request.POST['alt_no']
        acc.pincode = request.POST['pincode']
        acc.district = request.POST['district']
        acc.state = request.POST['state']
        acc.country = request.POST['country']
        acc.permanentaddress1 = request.POST['address1']
        acc.permanentaddress2 = request.POST['address2']
        acc.permanentaddress3 = request.POST['address3']
        acc.date = datetime.now()
        acc.save()
        return redirect('loginwelfare')
    else:
      messages.info(request, 'Password doesnt match. Register Again')
      return redirect('reg')









def Registration2(request):
    if request.method == 'POST':
        acc = restaurant_registration()
        acc.restaurantname = request.POST['rname']
        acc.location = request.POST['loname']
        acc.username = request.POST['uname']
        acc.email = request.POST['email']
        acc.password = request.POST['password']
        acc.mobile = request.POST['mobile']
        acc.alternativeno = request.POST['alt_no']
        acc.pincode = request.POST['pincode']
        acc.district = request.POST['district']
        acc.state = request.POST['state']
        acc.country = request.POST['country']
        acc.permanentaddress1 = request.POST['address1']
        acc.permanentaddress2 = request.POST['address2']
        acc.permanentaddress3 = request.POST['address3']
        acc.date = datetime.now()
        acc.save()
        return redirect('loginwelfare')
    else:
      messages.info(request, 'Password doesnt match. Register Again')
      return redirect('reg_rest')












def Admin_index(request):
    design = designation.objects.get(designation='Donar')
    don = user_registration.objects.filter(designation_id=design).filter(status='approved')
    return render(request, 'admin_temp/Admin_index.html',{'don':don})






def Admin_Msg_doner(request):
   
    design=designation.objects.get(designation="Donar")
    don = user_registration.objects.filter(designation_id=design).filter(status='approved')
    if request.method == 'POST':
        vars = message_admin()
        vars.message=request.POST.get('msg1')
        vars.date=datetime.now()
        vars.replay = "pending"
        vars.message_to_id=design.id
        donr_id = request.POST.get("doners")
        vars.donuser_id = donr_id
        vars.save()
    return redirect('Admin_index')


def Admin_Msg_ngo(request):
    design=designation.objects.get(designation="Ngo")
    if request.method == 'POST':
        vars = message_admin()
        vars.message=request.POST.get('msg2')
        vars.date=datetime.now()
        vars.replay = "pending"
        vars.message_to_id=design.id
        vars.save()
    return redirect('Admin_index')





def nadmin(request):
    return render(request, 'admin_temp/nadmin.html')

def Admin_doner_det(request):
    design = designation.objects.get(designation='Donar')
    don = user_registration.objects.filter(designation_id=design).filter(status='approved')
    des = designation.objects.get(designation='Donar')
    cs = user_registration.objects.filter(designation_id=des).filter(status='approved').order_by('-id')
    return render(request, 'admin_temp/Admin_doner_det.html',{'cs': cs,'don':don})

def Admin_ngo_det(request):
    design = designation.objects.get(designation='Donar')
    don = user_registration.objects.filter(designation_id=design).filter(status='approved')
    des = designation.objects.get(designation='Ngo')
    cs = user_registration.objects.filter(designation_id=des).filter(status='approved').order_by('-id')
    return render(request, 'admin_temp/Admin_ngo_det.html',{'cs':cs,'don':don})

def Admin_nofification(request):
    design = designation.objects.get(designation='Donar')
    don = user_registration.objects.filter(designation_id=design).filter(status='approved')
    des = designation.objects.all()
    cs = user_registration.objects.all().order_by('-id')
    count=user_registration.objects.all().count()
    return render(request, 'admin_temp/Admin_nofification.html',{'cs':cs,'count':count,'don':don})


def Admin_reject(request,id):
    pro_sts = user_registration.objects.filter(id=id).update(status ='rejected')
    return redirect('Admin_nofification')
   


def Admin_approve(request,id):
    al = user_registration.objects.filter(id=id).update(status ='approved')
    return redirect('Admin_nofification')



def Admin_logout(request):
    request.session.flush()
    return redirect("/")


def Admin_No_Card(request):
    design = designation.objects.get(designation='Donar')
    don = user_registration.objects.filter(designation_id=design).filter(status='approved')
    des = designation.objects.get(designation='Ngo')
    count2=user_registration.objects.all().count()
    return render(request, 'admin_temp/Admin_No_Card.html',{'count2':count2,'don':don})

def Admin_Notification_des_Card(request):
    design = designation.objects.get(designation='Donar')
    don = user_registration.objects.filter(designation_id=design).filter(status='approved')
    des = designation.objects.get(designation='Ngo')
    count=message_admin.objects.filter(message_to=des).count()
    des2 = designation.objects.get(designation='Donar')
    count2 = message_admin.objects.filter(message_to_id=des2).count()
    return render(request, 'admin_temp/Admin_Notification_des_Card.html',{'count':count,'count2':count2,'don':don})



def Admin_ngo_messages(request):
    design = designation.objects.get(designation='Donar')
    don = user_registration.objects.filter(designation_id=design).filter(status='approved')
    des = designation.objects.get(designation='Ngo')
    cs = message_admin.objects.filter(message_to_id=des).order_by('-id')
    
    return render(request, 'admin_temp/Admin_ngo_messages.html',{'cs':cs,'don':don})

def Admin_donar_messages(request):
    design = designation.objects.get(designation='Donar')
    don = user_registration.objects.filter(designation_id=design).filter(status='approved')
    des = designation.objects.get(designation='Donar')
    cs = message_admin.objects.filter(message_to_id=des).order_by('-id')
    
    return render(request, 'admin_temp/Admin_donar_messages.html',{'cs':cs,'don':don})

def Admin_donar_donation_history(request):
    design = designation.objects.get(designation='Donar')
    don = user_registration.objects.filter(designation_id=design).filter(status='approved')
    cs = doner_registration.objects.filter(status='approved').order_by('-id')
    return render(request, 'admin_temp/Admin_donar_donation_history.html',{'cs':cs,'don':don})


def Admin_restaurent_req_food_det(request):
    design = designation.objects.get(designation='Donar')
    don = user_registration.objects.filter(designation_id=design).filter(status='approved')
    cs = request_food.objects.all().order_by('-id')
    ngo=user_registration.objects.all()
    return render(request, 'admin_temp/Admin_restaurent_req_food_det.html',{'cs': cs,'don':don})

def Admin_reply_restaurent(request,id):
    if request.method == 'POST':
        rep=request.POST.get('reply')
        pro_sts = request_food.objects.filter(id=id).update(reason= rep,status ='approved')
    return redirect('Admin_restaurent_req_food_det')

def Admin_reason_restaurent(request,id):
    if request.method == 'POST':
        rereas=request.POST.get('replytwo')
        pro_sts = request_food.objects.filter(id=id).update(reason= rereas,status ='rejected')
    return redirect('Admin_restaurent_req_food_det')



def Donar_logout(request):
    request.session.flush()
    return redirect("/")


def Donar_index(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
            mem4 = user_registration.objects.filter(id=Tnr_id)
    adm=user_registration.objects.get(id=Tnr_id)
    return render(request, 'admin_temp/Donar_index.html',{'mem4':mem4,'adm':adm})   

def Donar_donation(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
            mem4 = user_registration.objects.filter(id=Tnr_id)
    adm=user_registration.objects.get(id=Tnr_id)
    return render(request, 'admin_temp/Donar_donation.html',{'adm':adm})


def Donar_donation_registration(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
            mem4 = user_registration.objects.filter(id=Tnr_id)
        if request.session.has_key('doid'):
            doid = request.session['doid']
      
            if request.method == 'POST':
                acc = doner_registration()
                acc.firstname = request.POST['fname']
                acc.lastname = request.POST['lname']
                acc.designation_id=doid
                acc.duser_id = Tnr_id
                acc.email = request.POST['email']
                acc.mobile = request.POST['mobile']
                acc.pincode = request.POST['pincode']
                acc.country = request.POST['country']
                acc.status = "pending"
                acc.permanentaddress1 = request.POST['address1']
                acc.permanentaddress2 = request.POST['address2']
                acc.payment = request.POST['pay']
                acc.message = request.POST['msg']
                acc.date = datetime.now()
                acc.save()
            return redirect('Doner_req_det')





def Donar_donation_det(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
            mem4 = user_registration.objects.filter(id=Tnr_id)
    cs = doner_registration.objects.filter(duser_id=Tnr_id).order_by('-id')
    adm=user_registration.objects.get(id=Tnr_id)
    return render(request, 'admin_temp/Donar_donation_det.html',{'cs':cs,'mem4':mem4,'adm':adm}) 


def Doner_req_det(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
            mem4 = user_registration.objects.filter(id=Tnr_id)
    des = designation.objects.get(designation='Donar')
    cs = doner_registration.objects.filter(duser_id=Tnr_id).order_by('-id')
    adm=user_registration.objects.get(id=Tnr_id)
    return render(request, 'admin_temp/Doner_req_det.html',{'cs': cs,'meme4':mem4,'adm':adm})

def Doner_admin_message(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
            mem4 = user_registration.objects.filter(id=Tnr_id)
    des = designation.objects.get(designation='Donar')
    cs = message_admin.objects.filter(donuser_id=Tnr_id).order_by('-id')
    adm=user_registration.objects.get(id=Tnr_id)
    return render(request, 'admin_temp/Doner_admin_message.html',{'cs':cs,'mem4':mem4,'adm':adm})

def Donar_admin_messages_replay(request,id):
    if request.method == 'POST':
        ngoreplay=request.POST.get('rep2')
        pro_sts = message_admin.objects.filter(id=id).update(replay = ngoreplay)
    return redirect('Doner_admin_message')








def Ngo_logout(request):
    request.session.flush()
    return redirect("/")


def Ngo_index(request):
    return render(request, 'admin_temp/Ngo_index.html')


def Ngo_No_Card(request):
    des = designation.objects.get(designation='Ngo')
    count2=doner_registration.objects.all().count()
    count=message_admin.objects.filter(message_to=des).count()
    return render(request, 'admin_temp/Ngo_No_Card.html',{'count2':count2,'count':count})


def Ngo_admin_messages(request):
    des = designation.objects.get(designation='Ngo')
    cs = message_admin.objects.filter(message_to_id=des).order_by('-id')
    
    return render(request, 'admin_temp/Ngo_admin_messages.html',{'cs':cs})


def Ngo_admin_messages_replay(request,id):
    if request.method == 'POST':
        ngoreplay=request.POST.get('rep')
        pro_sts = message_admin.objects.filter(id=id).update(replay = ngoreplay)
    return redirect('Ngo_admin_messages')


def Ngo_doner_det(request):
    des = designation.objects.get(designation='Donar')
    cs = doner_registration.objects.all().order_by('-id')
    return render(request, 'admin_temp/Ngo_doner_det.html',{'cs': cs})


def Ngo_nofification(request):
    
    des = designation.objects.all()
    cs = doner_registration.objects.all().order_by('-id')
    return render(request, 'admin_temp/Ngo_nofification.html',{'cs':cs})



def Ngo_reject(request,id):
    pro_sts = doner_registration.objects.filter(id=id).update(status ='rejected')
    return redirect('Ngo_nofification')
   


def Ngo_approve(request,id):
    al = doner_registration.objects.filter(id=id).update(status ='approved')
    return redirect('Ngo_nofification')



def Ngo_donation_history(request):
    cs = doner_registration.objects.filter(status='approved').order_by('-id')
    return render(request, 'admin_temp/Ngo_donation_history.html',{'cs':cs})



def Ngo_Admin_res_approved_food_det(request):
   
    
    cs = request_food.objects.filter(status='approved').order_by('-id')
    return render(request, 'admin_temp/Ngo_Admin_res_approved_food_det.html',{'cs': cs})



def Restaurant_logout(request):
    request.session.flush()
    return redirect("/")


def Restaurant_index(request):
    if 're_id' in request.session:
        if request.session.has_key('re_id'):
            re_id = request.session['re_id']
            mem1 = user_registration.objects.filter(id=re_id)
    rest=restaurant_registration.objects.get(id=re_id)
    return render(request, 'admin_temp/Restaurant_index.html',{'mem1':mem1,'rest':rest})  


def Restaurant_Card(request):
    if 're_id' in request.session:
        if request.session.has_key('re_id'):
            re_id = request.session['re_id']
            mem1 = user_registration.objects.filter(id=re_id)
    count2=request_food.objects.filter(restaurantname_id=re_id).count()
    rest=restaurant_registration.objects.get(id=re_id)
    return render(request, 'admin_temp/Restaurant_Card.html',{'mem1':mem1,'count2':count2,'rest':rest})  


def Restaurant_req_food(request):
    if 're_id' in request.session:
        if request.session.has_key('re_id'):
            re_id = request.session['re_id']
            mem1 = user_registration.objects.filter(id=re_id)
    resto=restaurant_registration.objects.get(id=re_id)
    rest=restaurant_registration.objects.get(id=re_id)
    return render(request, 'admin_temp/Restaurant_req_food.html',{'resto':resto,'mem1':mem1,'rest':rest})  



def Request_res_food(request):
    if 're_id' in request.session:
        if request.session.has_key('re_id'):
            re_id = request.session['re_id']
            mem1 = user_registration.objects.filter(id=re_id)
    resto=restaurant_registration.objects.get(id=re_id)
    if request.method == 'POST':
        acc = request_food()
        acc.restaurantname_id = re_id
        acc.date = datetime.now()
        acc.status = "pending"
        acc.reason = "pending"
        acc.mobile = request.POST['mobile']
        acc.location = request.POST['loc']
        acc.quantity = request.POST['qnt']
        acc.cookedtime = request.POST['ctime']
        acc.save()
        return redirect('Restaurant_req_food')





def restaurent_requested_food_det(request):
    if 're_id' in request.session:
        if request.session.has_key('re_id'):
            re_id = request.session['re_id']
            mem1 = user_registration.objects.filter(id=re_id)
    cs = request_food.objects.filter(restaurantname_id=re_id).order_by('-id')
    rest=restaurant_registration.objects.get(id=re_id)
    return render(request, 'admin_temp/restaurent_requested_food_det.html',{'cs': cs,'mem1':mem1,'rest':rest})


def Restaurent_Admin_messages(request):
    if 're_id' in request.session:
        if request.session.has_key('re_id'):
            re_id = request.session['re_id']
            mem1 = user_registration.objects.filter(id=re_id)
    cs = request_food.objects.filter(restaurantname_id=re_id).filter(status='approved').order_by('-id')
    rest=restaurant_registration.objects.get(id=re_id)
    return render(request, 'admin_temp/Restaurent_Admin_messages.html',{'cs': cs,'mem1':mem1,'rest':rest})
