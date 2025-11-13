from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from sqlalchemy import create_engine
from models import DBSession, Base, get_tm_session
import pyramid_tm

if __name__ == '__main__':
    # 1. Setup Koneksi Database (SQLite)
    # File database akan muncul dengan nama 'tutorial.sqlite'
    engine = create_engine('sqlite:///tutorial.sqlite')
    
    # 2. Ikat session dan base ke engine
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    
    # 3. Buat Tabel jika belum ada (Create Table)
    Base.metadata.create_all(engine)

    with Configurator() as config:
        config.include('pyramid_chameleon')
        
        # PENTING: Aktifkan Transaction Manager (agar save data otomatis aman)
        config.include('pyramid_tm')

        # Setup agar setiap request punya properti 'dbsession' (Standard Pyramid)
        config.add_request_method(
            lambda r: get_tm_session(DBSession, r.tm),
            'dbsession',
            reify=True
        )

        config.add_route('home', '/')
        config.add_route('add_page', '/add')
        
        config.scan('views')
        app = config.make_wsgi_app()
    
    print("Server berjalan di http://localhost:6543")
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()