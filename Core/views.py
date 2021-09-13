from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Videos, Usuarios, Comentarios
from .forms import Criar_UsuariosForms
# Create your views here.
#Aqui e a parte do index so.
def Index(request):
    """Aqui vai mostrar todos os videos cadastrados."""
    videos = Videos.objects.all()
    if request.method == 'POST':
        busca = request.POST['tag']
        videos = Videos.objects.filter(Categoria__icontains = busca)
        print(videos)
        if not videos:
            print('vaziu')
            videos = Videos.objects.filter(Titulo__icontains = busca)
    dados = {'videos':videos}
    return render(request,'Index.html',dados)
#------------------------------------------------------

#Aqui e aparte de crias os usuarios e login.
def Criar_Usuarios(request):
    """A parte da criaçao dos usuarios com uma 'Validaçao simples. '"""
    if request.method == 'POST':
        nome = request.POST['Nome']
        email = request.POST['Email']
        senha_1 = request.POST['senha_1']
        senha_2 = request .POST['senha_2']

        if not nome.strip():
            return redirect('Cadastro')
        if not email.strip():
            return redirect('Cadastro')
        if senha_1 != senha_2:
            return redirect('Cadastro')
        if User.objects.filter(email=email).exists():
            print('ja cadastrado')
        user = User.objects.create_user(username=nome,email=email,password=senha_1)
        user.save()
        return redirect('Login')
    else:
        return render(request,'Cadastrar.html')


def Login(request):
    if request.method == 'POST':
        email = request.POST['Email']
        senha = request.POST['Senha']
        if email == '' or senha == '':
            redirect('Login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request,username=nome,password=senha)
            if user is not None:
                auth.login(request,user)
                return redirect('Dashbord')
    return  render(request,'Login.html')

def Sair(request):
    auth.logout(request)
    return redirect('Index')

#-----------------------------------------------------

# Aqui começa a parte dos perfil a Criaçao do perfil,dos videos e o dashbord

def Perfil(request):
    """Criaçao do perfil com foto e nikename e tambem podendo editar"""
    if request.user.is_authenticated:
        nike = request.POST.get('Nikename')
        foto = request.FILES.get('Foto')
        id = request.user
        perfil_id = request.POST.get('Perfil_id')
        if perfil_id:
            perfil = Usuarios.objects.get(id=perfil_id)
            if id == perfil.Usuario:
                perfil.Nikename = nike
                if foto:
                    perfil.Foto = foto
                perfil.save()
                return redirect('Dashbord')
        else:
            id = request.user.id
            nike =  request.POST['Nikename']
            foto = request.FILES['Foto']
            user = get_object_or_404(User,pk=id)
            perfil_salvar = Usuarios.objects.create(Nikename=nike,Foto=foto,Usuario=user)
            perfil_salvar.save()
            return redirect('Dashbord')
    else:
        Criar = Criar_UsuariosForms
        dados = {'Criar': Criar}

    return render(request,'Dashbord.html')

def Cadastrar_video(request):
    """Aqui e a parte para postar videos so quem esta logado pode postar o videos.
        e tamabem editar eles se escreveu o nome errado ou postou o video errado."""
    if request.user.is_authenticated:
        if request.method == 'POST':
            id = request.user.id
            titulo = request.POST['Titulo']
            categoria = request.POST['Categoria']
            descricao = request.POST['Descricao']
            video = request.FILES['Video']
            user = get_object_or_404(User,pk=id)
            salvar_video = Videos.objects.create(Usuario=user,Titulo=titulo,Categoria=categoria,Descricao=descricao, Video=video)
            salvar_video.save()
            return redirect('Dashbord')
        else:
            return redirect('Dashbord')
    else:
        return redirect('Login')

def Dashbord(request):
    """Aqui e o seu DashBord onde esta todos os videos que voce postou."""
    if request.user.is_authenticated:
        id = request.user.id
        usuario = Usuarios.objects.all().filter(Usuario=id)

        video = Videos.objects.all().filter(Usuario=id)
        Criar = Criar_UsuariosForms
        dados = {'usuario':usuario,'Criar':Criar,'video':video}

        return render(request,'Dashbord.html',dados)
    else:
        return redirect('Index')

def Excluir(request,vid_id):
    if request.user.is_authenticated:
        video =  Videos.objects.get(id=vid_id)
        video.delete()
        return redirect('Dashbord')
    else:
        return render(request,'Index.html')
#---------------------------------------------------------------

#aqui e a parte dos detalhes dos videos e tambem os comentarios e as paginas dos usuarios que postaram. .
def Detalhes(request,vid_id):
    video = Videos.objects.get(id=vid_id)
    comentario = Comentarios.objects.all().filter(Video=vid_id)
    nike = Usuarios.objects.all()
    dados = {'video':video,'comentario':comentario,'nike':nike}
    return render(request,'Detalhes.html',dados)


def Comentar(request,video_id):
    if request.user.is_authenticated:
       if request.POST:
           id = request.user.id
           user = get_object_or_404(User,pk=id)
           video = Videos.objects.get(id=video_id)
           vid_id = video_id
           cometario = request.POST['Comentario']
           print(user,cometario)

           salvar_comentario = Comentarios.objects.create(Usuario=user,Video=video,Comentario=cometario)
           salvar_comentario.save()
           return redirect(f'/{vid_id}')
       else:
           return render(request,'Detalhes.html')
    else:
        return render(request,'Login.html')

def Pagina_dos_Videos(request,nike_id):
    perfil = Usuarios.objects.get(id=nike_id)
    video = Videos.objects.all().filter(Usuario=perfil.Usuario)
    video_all = Videos.objects.all().exclude(Usuario=perfil.Usuario)
    dados = {'perfil':perfil, 'video':video, 'video_all':video_all}

    return render(request,'pagina_do_perfil.html',dados)

#----------------------------------------------
#Aqui e a parte de pesquisa
def pesquisa_de_vida(resquest,tag):
    pass