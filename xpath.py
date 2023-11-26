from info import username

xpath = {
    'login' : {
        'username' : "//input[@name='username']",
        'password' : "//input[@name='password']",
        'submit' : "//button[@type='submit']",
        'verification' : "//input[@name='verificationCode']",
        'backup_button' : "//button[text()='backup codes']",
        'confirm_button' : "//button[text()='Confirm']",
        'save_login_button' : "//div[text()='Not Now']",
        'notif_button' : "//button[text()='Not Now']"
    },
    'home_page' : {
        'direct_button' : f"//a[text()='{username}']"
    }
}

def get_xpath(data, element):
    return xpath[data][element]