from flask_blog import db, User, Post

if __name__ == '__main__':
    db.create_all()

    user_1 = User(username='Zhangda', email='just4xzd1995@gmail.com', password='passwd')
    db.session.add(user_1)
    db.session.commit()

    user = User.query.all()
    print('User info:', user)
    # [User('Zhangda', 'just4xzd1995@gmail.com', 'default.jpg')]

    user = User.query.filter_by(username='Zhangda').first()
    print('User Id:', user.id)
    # 1

    user = User.query.get(1)
    print('User posts:', user.posts)
    # []

    post_1 = Post(title='Blog 1', content='First Post Content!', user_id=user.id)
    db.session.add(post_1)
    db.session.commit()

    post = Post.query.first()
    print('Post title:', post.title)
    # 'Blog 1'
    
    db.drop_all()