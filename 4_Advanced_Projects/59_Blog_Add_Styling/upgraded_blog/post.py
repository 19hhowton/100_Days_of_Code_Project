class Post:
    """Create Post object for each post."""
    def __init__(self, post_id, title, subtitle, body, image_url, date, author):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body
        self.image_url = image_url
        self.date = date
        self.author = author