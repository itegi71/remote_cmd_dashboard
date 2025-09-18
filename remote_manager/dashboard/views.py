from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SSHCommandForm
from.models import Commandlog
from .utils.ssh_manager import SSHClientManager

def dashboard_home(request):
    print(request.method)
    #main viewfor handling ssh connections and command execcutions 
    if request.method =='POST':
        form=SSHCommandForm(request.POST)

        if form.is_valid():
            hostname=form.cleaned_data['hostname']
            port=form.cleaned_data['port']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            use_predefined=form.cleaned_data['use_predefined']
            command=form.cleaned_data['predefined_command'] if use_predefined else form.cleaned_data['custom_command']

            try:
                #use my OOP SSH manager 
                ssh_manager=SSHClientManager(hostname,port,username,password)
                ssh_manager.connect()
                output=ssh_manager.execute_command(command)
                ssh_manager.close()

                #save the command log to db
                Commandlog.objects.create(
                    Server_ip=hostname,
                    command=command,
                    output=output
                )

                #pass result to template

                return render(request,'dashboard/result.html',{
                    'hostname':hostname,
                    'command':command,
                    'output':output
                })
            except Exception as e:
                messages.error(request,f"Connection failed:{e}")
                return redirect('dashboard_home')
    else:
            form=SSHCommandForm()

    return render(request,'dashboard/index.html',{'form':form})

def command_logs(request):
     logs =Commandlog.objects.all().order_by('-timestamp')
     return render(request,'dashboard/command_logs.html',{'logs':logs})

