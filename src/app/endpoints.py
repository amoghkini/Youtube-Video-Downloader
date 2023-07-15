from flask import Flask


from restapis import (about_us_api, dashboard_api, home_api, login_api, logout_api, my_profile_api,
                      password_change_api, password_reset_api, password_reset_request, sign_up_api, verify_user_api)

def register_endpoints(app: Flask) -> None:

    app.add_url_rule("/", view_func=home_api.HomeAPI.as_view("home_api"))
    app.add_url_rule("/about", view_func=about_us_api.AboutUsAPI.as_view("about_us_api"))
    app.add_url_rule("/dashboard", view_func=dashboard_api.DashboardAPI.as_view("dashboard_api"))
    app.add_url_rule("/user/login", view_func=login_api.LogInAPI.as_view("login_api"))
    app.add_url_rule("/user/logout", view_func=logout_api.LogOutAPI.as_view("logout_api"))
    app.add_url_rule("/user/profile", view_func=my_profile_api.MyProfileAPI.as_view("my_profile_api"))
    app.add_url_rule("/user/password_change", view_func=password_change_api.PasswordChangeAPI.as_view("change_password_api"))
    app.add_url_rule("/user/password_reset/<token>", view_func=password_reset_api.PasswordResetAPI.as_view("reset_password_api"))
    app.add_url_rule("/user/password_reset_request", view_func=password_reset_request.PasswordResetRequestAPI.as_view("reset_password_request_api"))
    app.add_url_rule("/user/signup", view_func=sign_up_api.SignUpAPI.as_view("sign_up_api"))
    app.add_url_rule("/user/verify/<token>", view_func=verify_user_api.VerifyUserAPI.as_view("verify_email_api"))