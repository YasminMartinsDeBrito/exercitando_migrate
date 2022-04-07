def init_app(app, db):

    @app.cli.command('add_music')
    def insert_music():

        """ Insert a new music"""
        from models import Music
        from datetime import datetime

        with app.app_context():
            new_music = Music(title="you could be mine", duration=datetime.time(datetime(1,1,1,0,5,44)))
            db.session.add(new_music)
            db.session.commit()
            print(f"Inserted Music\nName: {new_music.title}\nDuration: {new_music.duration}")

            