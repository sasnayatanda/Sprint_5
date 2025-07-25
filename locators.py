from selenium.webdriver.common.by import By

# Форма регистрации
REGISTER_FORM_NAME_FIELD = (By.XPATH, '//input[@type="text" and @name="name"]')
REGISTER_FORM_EMAIL_FIELD = (By.XPATH, '//input[@type="email" and @name="email"]')
REGISTER_FORM_PASSWORD_FIELD = (By.XPATH, '//input[@type="password" and @name="password"]')
REGISTER_SUBMIT_BUTTON = (By.XPATH, '//button[.//span[normalize-space()="Зарегистрироваться"]]')

# Форма входа
LOGIN_FORM_EMAIL_FIELD = (By.XPATH, '//input[@type="email" and @name="email"]')
LOGIN_FORM_PASSWORD_FIELD = (By.XPATH, '//input[@type="password" and @name="password"]')
LOGIN_SUBMIT_BUTTON = (By.XPATH, '//button[.//span[normalize-space()="Войти"]]')

# Сообщения
REGISTRATION_SUCCESS_MESSAGE = (By.XPATH, '//p[contains(normalize-space(), "Вы успешно зарегистрированы")]')
INVALID_CREDENTIALS_MESSAGE = (By.XPATH, '//p[contains(normalize-space(), "Неверный логин или пароль")]')

# Элементы навигации
ACCOUNT_LOGIN_BUTTON = (By.XPATH, '//a[contains(@href, "/login")]')
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[contains(@href, "/account/profile")]')
BURGER_MENU_ICON = (By.XPATH, '//img[@alt="Stellar Burgers"]')

# Меню конструктора
MENU_BUNS_SECTION = (By.XPATH, '//h2[contains(normalize-space(), "Булки")]')
MENU_SAUCES_SECTION = (By.XPATH, '//h2[contains(normalize-space(), "Соус")]')
MENU_FILLINGS_SECTION = (By.XPATH, '//h2[contains(normalize-space(), "Наполнитель")]')

# Кнопка выхода
LOGOUT_BUTTON = (By.XPATH, '//button//span[normalize-space()="Выход"]')