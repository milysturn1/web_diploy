from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import *
from .forms import *


def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()

    context = {
        "title": "Главная страница",
        "categories": categories,
        "articles": articles
    }

    return render(request, "blog/index.html", context)


def category_page_view(request, category_id):
    # filter() --- брать по условию
    articles = Article.objects.filter(category=category_id)
    trends = Article.objects.all().order_by('views')
    category = Category.objects.get(id=category_id)

    context = {
        "title": f"Катагория: {category.title}",
        "articles": articles,
        "trends": trends,
        "category_name": category.title
    }

    return render(request, "blog/category_page.html", context)


def article_detail_view(request, article_id):
    article = Article.objects.get(id=article_id)
    last = Article.objects.all().order_by('-created_at')
    if request.user.id != article.author.id:
        article.views += 1
        article.save()
    comments = Comment.objects.filter(article=article.id)

    context = {
        "title": f"Статья: {article.title}",
        "article": article,
        "last_articles": last,
        "comments": comments
    }
    if request.user.is_authenticated:
        context.update({
            "comment_form": CommentForm()
        })

    return render(request, "blog/article_detail.html", context)


def about_us_page_view(request):
    return render(request, "blog/about_us.html")


def our_teams_page_view(request):
    return render(request, "blog/our_team.html")


def our_services_page_view(request):
    return render(request, "blog/services.html")


@login_required(login_url='login')
def add_article(request):
    if request.method == "POST":
        form = ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, "Статья успешно добавлена !")
            return redirect('article_detail', article.id)
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect('add_article')
    else:
        form = ArticleForm()

    context = {
        'title': "Добавить статью",
        'form': form
    }

    return render(request, "blog/add_article.html", context)


def register_user_view(request):
    if request.method == "POST":
        form = RegistrationUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            messages.success(request, "Вы успешно прошли регистрацию !")
            return redirect('login')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect('register')
    else:
        form = RegistrationUserForm()

    context = {
        "title": "Регистрация пользователя",
        "form": form
    }

    return render(request, "blog/register.html", context)


def login_user_view(request):
    if request.method == "POST":
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                messages.success(request, "Вы успешно зашли в аккаунт !")
                return redirect('index')
            else:
                messages.error(request, "Логин или пароль неправильный !")
                return redirect('login')
        else:
            messages.error(request, "Логин или пароль неправильный !")
            return redirect('login')
    else:
        form = LoginUserForm()

    context = {
        "title": "Войти в аккаунт",
        "form": form
    }

    return render(request, "blog/login.html", context)


@login_required(login_url='login')
def logout_user_view(request):
    logout(request)
    messages.info(request, "Вы вышли с аккаунта !")
    return redirect('index')


@login_required(login_url='login')
def update_article_view(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        form = ArticleForm(instance=article,
                           data=request.POST,
                           files=request.FILES)
        if form.is_valid():
            article = form.save()
            messages.info(request, "Статья успешно обновлена !")
            return redirect("article_detail", article.pk)
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect("update_article", article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        "title": "Изменить статью",
        "form": form
    }

    return render(request, "blog/add_article.html", context)


@login_required(login_url='login')
def article_delete(request, article_id):
    article = Article.objects.get(pk=article_id)

    if request.method == 'POST':
        article.delete()
        messages.info(request, "Статья удалена !")
        return redirect("index")

    context = {
        "title": "Удаление статьи",
        "article": article
    }

    return render(request, "blog/delete_article.html", context)


def profile_view(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)

    context = {
        "user": user,
        "profile": profile,
        "title": "Профиль пользователя"
    }

    return render(request, "blog/profile.html", context)


@login_required(login_url='login')
def update_profile_view(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)

    if request.method == "POST":
        user_form = UserForm(instance=user, data=request.POST)
        profile_form = ProfileForm(instance=profile,
                                   data=request.POST,
                                   files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.info(request, "Данные профиля успешно обновлены !")
            return redirect("profile", user.id)
        else:
            for field in user_form.errors:
                messages.error(request, user_form.errors[field].as_text())
            for field in profile_form.errors:
                messages.error(request, profile_form.errors[field].as_text())
            return redirect("update_profile", user.id)
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "title": "Изменить профиль"
    }
    return render(request, "blog/edit_profile.html", context)


@login_required(login_url='login')
def save_comment(request, article_id):
    article = Article.objects.get(id=article_id)
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.article = article
        comment.save()
        messages.info(request, "Комментарий успешно сохранен !")
        return redirect("article_detail", article_id)
    else:
        messages.error(request, "Что-то пошло не так !")
        return redirect("article_detail", article_id)
