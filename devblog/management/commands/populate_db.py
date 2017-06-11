from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from devblog.models import Post, Comment

content1 = "Cras ullamcorper, justo quis pretium mollis, odio dui commodo ante, eu interdum risus lectus tincidunt ipsum. In in nibh porttitor, luctus mi sit amet, tempus justo. Interdum et malesuada fames."
content2 = "Pellentesque sit amet lorem odio. In eleifend risus malesuada commodo fringilla. Vivamus a accumsan neque. Curabitur elementum urna sed varius blandit. Sed tincidunt nisi metus, non egestas massa convallis a. Nulla gravida ex id blandit dapibus. Nulla dictum enim neque, sed condimentum lorem lobortis eget. Ut libero metus, ultrices eu. "
content3 = """Nullam porta ex magna, a vulputate metus egestas cursus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nulla facilisi. Maecenas et sapien ut justo dapibus gravida. Sed rhoncus magna arcu, sed dapibus tortor finibus pharetra. Sed vel vehicula lectus, id bibendum nisi. Donec sagittis dui ante, vitae posuere lacus blandit at. Quisque faucibus tincidunt turpis.

Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Proin facilisis sed nulla a gravida. Orci varius natoque penatibus et. """

class Command(BaseCommand):
    args = '<no arguments>'
    help = 'Just fills the database with dummy data'

    def _create_users(self):
        user1 = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user1.save()

        user2 = User.objects.create_user('hulk', 'hoggan@hulk.com', 'hulkpassword')
        user2.save()

        user3 = User.objects.create_user('nacho', 'nacho@elmacho.com', 'machopassword')
        user3.save()

    def _create_posts(self):
        posts=[
        Post(author_id=1, title="Dummy Post 1", content=content1),
        Post(author_id=2, title="Dummy Post 2", content=content2),
        Post(author_id=2, title="Dummy Post 3", content=content1),
        Post(author_id=1, title="Another Dummy Post", content=content3),
        Post(author_id=2, title="One more Dummy Post", content=content2),
        Post(author_id=1, title="And another Dummy Post", content=content1),
        Post(author_id=3, title="Just one more Dummy Post", content=content1),
        Post(author_id=3, title="Wtf more Posts Dummy Post", content=content2),
        Post(author_id=2, title="Im tired of Dummy Posts", content=content3),
        Post(author_id=2, title="Here lies another Dummy Post", content=content2),
        Post(author_id=1, title="JUST STOP Loocking for moar Dummy Posts", content=content2),
        Post(author_id=3, title="No comment, just  Dummy Posts", content=content1)]
        # rellenamos la base de datos con un monton de Posts 12 x 15
        for i in range (15):
            for x in posts:
                x.save()

    def handle(self, *args, **options):
        self._create_posts()
        self._create_users()
