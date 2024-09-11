# Cookbook API

The Cookbook API is a back-end service for a recipe management application. It provides a RESTful API for handling user profiles, posts (formerly recipes), comments, likes, and followers. This API allows third-party applications to interact with the database, enabling functionalities like recipe management, user interactions, and more.

## Features

### Profile Management
- **List Profiles**: Retrieve a list of all user profiles with associated statistics.
- **Retrieve Profile**: Get detailed information about a specific user profile.
- **Update Profile**: Update user profile details.
- **Create Profile**: Create a new user profile.

### Post Management
- **List Posts**: Get a list of all posts with annotations for likes and comments.
- **Retrieve Post**: Get detailed information about a specific post.
- **Create Post**: Add a new post, including recipe details.
- **Update Post**: Modify an existing post.
- **Delete Post**: Remove a post from the database.

### Comment Management
- **List Comments**: Retrieve comments for a specific post.
- **Create Comment**: Add a new comment to a post.
- **Retrieve Comment**: Get detailed information about a specific comment.
- **Update Comment**: Modify an existing comment.
- **Delete Comment**: Remove a comment from the database.

### Like Management
- **List Likes**: Retrieve all likes for posts.
- **Create Like**: Like a post.
- **Delete Like**: Remove a like from a post.

### Follower Management
- **List Followers**: Get a list of all followers for a user.
- **Create Follower**: Follow a user.
- **Delete Follower**: Unfollow a user.

## Authentication and User Capabilities

### Authentication
- **Login**: Secure user authentication to access API endpoints.
- **Logout**: End the user session.
- **Sign Up**: Register a new user.

### User Capabilities
- **Profile Management**: Users can create, update, and view their profiles.
- **Post Management**: Users can add, update, and delete their own posts, which include recipe details like ingredients and instructions.
- **Commenting**: Users can add, edit, and delete comments on posts.
- **Liking Posts**: Users can like and unlike posts.
- **Following**: Users can follow and unfollow other users.

## Technologies

- **Backend Framework**: Django (Python)
- **Database**: PostgreSQL
- **Deployment**: Heroku

## Testing

### Manual Testing

| Test Case                             | Description                                                | Result         |
|---------------------------------------|------------------------------------------------------------|----------------|
| **Profile List Endpoint**              | Verify that the list of profiles can be retrieved.         | Pass           |
| **Profile Detail Endpoint**            | Ensure details of a single profile are correctly displayed. | Pass           |
| **Post List Endpoint**                 | Check if posts are listed with annotations.               | Pass           |
| **Post Detail Endpoint**               | Confirm detailed view of a specific post.                 | Pass           |
| **Comment Creation**                  | Test if new comments can be added to posts.               | Pass           |
| **Like Management**                   | Ensure likes can be added and removed from posts.         | Pass           |
| **Follower Management**               | Verify users can follow and unfollow other users.         | Pass           |
| **Authentication**                    | Test login, registration, and logout functionalities.      | Pass           |



### Bugs Resolved

| Issue Description                                                   | Resolution                                                                                          |
|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| **CSRF Failed: Origin Checking Failed**                            | Added the appropriate domains to `CSRF_TRUSTED_ORIGINS` in `settings.py` to include both localhost and the deployed URL. |
| **CORS Configuration Issues**                                      | Updated `CORS_ALLOWED_ORIGIN_REGEXES` to include correct regex patterns for development (Gitpod) and production environments. Ensured correct `CLIENT_ORIGIN_DEV` handling. |
| **400 Bad Request on Heroku Deployment**                           | Verified and corrected `ALLOWED_HOSTS` and other environment variables on Heroku. Ensured they are set without extraneous quotation marks. |
| **Duplicate CORS Allowed Origin Regexes**                          | Removed duplicated `CORS_ALLOWED_ORIGIN_REGEXES` and ensured only the necessary settings are present according to the latest instructions. |



### Bugs Unresolved

- No known unresolved bugs at this time.

### Code Validation

| Validator        | Results                                                          |
|------------------|------------------------------------------------------------------|
| **Python**       | No issues detected using `pep8ci` for style guide compliance.   |

## Version Control

- **Git & GitHub**: Git and GitHub are used for version control throughout the development process. Commit messages are used to document changes and progress, with regular commits for feature additions, bug fixes, and updates.

## Deployment

### Deployment Process

To deploy the API on Heroku, follow these steps:

1. **Create and Configure Heroku App:**
   - Sign up or log in to [Heroku](https://www.heroku.com/).
   - Create a new app from the Heroku Dashboard, specifying a unique name and region.
   - Add necessary Config Vars:
     - `DATABASE_URL`: Your PostgreSQL database URL.
     - `SECRET_KEY`: A new, secure key for production.
     - `CLOUDINARY_URL`: Your Cloudinary URL for image hosting.
     - Optionally, add `ALLOWED_HOST` and `CLIENT_ORIGIN_DEV`.

2. **Prepare Your Project:**
   - Install dependencies:
     ```bash
     pip3 install dj_database_url psycopg2 gunicorn django-cors-headers
     ```
   - Update `settings.py` to configure database, CORS, and JWT settings.
   - Create a `Procfile` with the following content:
     ```
     release: python manage.py makemigrations && python manage.py migrate
     web: gunicorn cookbookapi3.wsgi
     ```
   - Update `requirements.txt`:
     ```bash
     pip freeze --local > requirements.txt
     ```

3. **Deploy to Heroku:**
   - Connect your GitHub repository to the Heroku app.
   - Deploy the app manually or enable automatic deploys.
   - Run migrations in the terminal:
     ```
     python manage.py migrate
     ```

4. **Monitor and Scale:**
   - Use the Heroku Dashboard to monitor performance and scale dynos as needed.



## Credits

- **References:**
  - [Django Documentation](https://docs.djangoproject.com/en/stable/)
  - [Django REST Framework Documentation](https://www.django-rest-framework.org/)
  - [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-django)

