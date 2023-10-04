import os

post_folder = "blog_posts"
if not os.path.exists(post_folder):
    os.makedirs(post_folder)

def create_blog_post(title, content):
    post_filename = os.path.join(post_folder, f"{title}.txt")  # Include the folder path
    with open(post_filename, "w") as file:
        file.write(content)
    print(f"New blog post '{title}' created!")

def read_blog_post(title):
    post_filename = os.path.join(post_folder, f"{title}.txt")  # Include the folder path
    if os.path.exists(post_filename):
        with open(post_filename, "r") as file:
            content = file.read()
        print(f"--- {title} ---")
        print(content)
    else:
        print(f"Blog post '{title}' does not exist.")

def edit_blog_post(title, new_content):
    post_filename = os.path.join(post_folder, f"{title}.txt")  # Include the folder path
    if os.path.exists(post_filename):
        with open(post_filename, "w") as file:
            file.write(new_content)
        print(f"Blog post '{title}' edited successfully!")
    else:
        print(f"Blog post '{title}' does not exist.")


#mainmenu
while True:
    print("\nContent Management System Menu:")
    print("1. Create a new blog post")
    print("2. Read a blog post")
    print("3. Edit a blog post")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        title = input("Enter the title of the new blog post: ")
        content = input("Enter the content of the new blog post: ")
        create_blog_post(title, content)
    elif choice == '2':
        title = input("Enter the title of the blog post to read: ")
        read_blog_post(title)
    elif choice == '3':
        title = input("Enter the title of the blog post to edit: ")
        new_content = input("Enter the updated content: ")
        edit_blog_post(title, new_content)
    elif choice == '4':
        print("Exiting the CMS. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4).")
