def apply_design():
    custom_css = """
    <style>
        .stApp {
            background-color: #f7f7f7;
        }
        .stButton>button {
            background-color: #5e97b0;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #427d8e;
        }
        /* Add other custom CSS styles here */
    </style>
    """

    background_image = "background_image.jpg"  # Replace with your image
    background_css = f"""
    <style>
        .reportview-container {{
            background: url({background_image});
            background-size: cover;
        }}
    </style>
    """

    sun_icon = '<img src="images/sun_icon.png" width="30" height="30">'
    moon_icon = '<img src="images/moon_icon.png" width="30" height="30">'

    return custom_css, background_css, sun_icon, moon_icon
