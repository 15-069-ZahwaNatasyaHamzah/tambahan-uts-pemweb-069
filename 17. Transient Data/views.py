from pyramid.view import view_config

@view_config(route_name='home', renderer='home.pt')
def home_view(request):
    # 1. Cek apakah di saku memori (session) sudah ada 'counter'
    if 'counter' not in request.session:
        request.session['counter'] = 0
    
    # 2. Tambah angkanya
    request.session['counter'] += 1
    
    # 3. Kirim ke layar
    return {'counter': request.session['counter']}