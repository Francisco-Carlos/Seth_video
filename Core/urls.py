from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index, name='Index'),
    #aqui e a parte de cadastrar um usuario,fazer login,sair do seu acesso
    path('Cadastrar',views.Criar_Usuarios, name='Cadastrar'),
    path('Login',views.Login, name='Login'),
    path('Sair', views.Sair, name='Sair'),

    #aqui e para vocer ver o seu perfil e editar ele, e cadastrar um video
    path('Dashbord',views.Dashbord, name='Dashbord'),
    path('Perfil',views.Perfil, name='Perfil'),
    path('Cadastrar_video', views.Cadastrar_video, name='Cadastrar_video'),

    #aqui para baixo e para ver detalhes,e comentarios, e perfil dos videos

    path('<int:vid_id>',views.Detalhes,name='Detalhes'),
    path('Comentario,<int:video_id>',views.Comentar,name='Comentario'),
    path('perfil/<int:nike_id>',views.Pagina_dos_Videos, name='Perfil_do_video'),
]