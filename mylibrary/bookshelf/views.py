from django.views.generic import (CreateView, DetailView, ListView, TemplateView,
                                  UpdateView)

from .forms import AuthorForm, BookForm
from .models import Author, Book


class WelcomeView(TemplateView):
    template_name = 'welcome.html'

class AuthorCreateView(CreateView):
    model = Author
    template_name = 'my-author-create.html'
    form_class = AuthorForm
    success_url = '/my-books'

class BooksView(ListView):
    model = Book
    template_name = 'my-books.html'


class BookDetailByIdView(DetailView):
    model = Book
    template_name = 'my-book-detail.html'


class BookDetailByCodeView(DetailView):
    model = Book
    template_name = 'my-book-detail.html'
    
    def get_object(self):
        return Book.objects.get(code=self.kwargs['code'])


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'my-book-edit.html'
    form_class = BookForm
    success_url = '/my-books'
    
class BookCreateView(CreateView):
    model = Book
    template_name = 'my-book-create.html'
    form_class = BookForm
    success_url = '/my-books'
    https://streamm4u.ws/movies/what-every-frenchwoman-wants-1986.od6w7.html
    https://www.google.com/search?rlz=1C1ONGR_enIN974IN974&sxsrf=AOaemvKZMbm-ST1LTqVhG5trzHD2YbSaNA:1641110930678&q=gianfranco+mingozzi+bellissimo:+images+of+the+italian+cinema&stick=H4sIAAAAAAAAAONgFuLSz9U3MEnJKMzJU-LVT9c3NEwrNymrMCgw0ZLITrbSL0jNL8hJBVJFxfl5Vrn5ZZmpxY8YPzNyC7z8cU9Y6iXjpDUnrzE-YuTCqVpIj4vNNa8ks6RSiE-KhwvJQiMRLoiVWUVZVTlFhRUCX_ZNZ1TqZTTK2HVp2jm2JEGRdAaGFOtQBykjwdsqmy2yd7621xLiYvcs9slPTswRXHmo959g00t7LWEujpDEivy8_NxKwYXXXiR8jn1nr6TI-euV5gHxl-_tBavV_s3_EW_hIMGmwKDBYHj5GvsDtniuA1oMQRwg5xiVVeQFgR2Wnp6UbVF0gJGpad-KQ2wsHIwCDFZMGkxVTBxMPItYbdIzE_PSihLzkvMVcjPz0vOrqjIVklJzcjKLizNz860UMnMT01OLFfLTFEoyUhUySxJzgBoUkjPzUnMTJ7AxAgDzbTbWcAEAAA&sa=X&sqi=2


    https://watchcartoononline.bz/tvshows/huntik-secrets-and-seekers-season-1/
    Laura Prepon
    huntik-secrets-and-seekers

    Testing Engineer 809108BR
    secrets of teenage girls 1980
    https://www.vintagepornfun.com/2020/10/14/sechs-schwedinnen-von-der-tankstelle-six-swedes-at-a-pump-1980-en/
    
