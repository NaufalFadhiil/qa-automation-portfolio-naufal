class LoginPage {

    elements = {
        usernameInput: () => cy.get('input[name="username"]'),
        passwordInput: () => cy.get('input[name="password"]'),
        loginButton: () => cy.get('button[type="submit"]'),
        errorMessage: () => cy.contains('Invalid credentials'),
        requiredMessage: () => cy.contains('Required'),
        forgotPassword: () => cy.contains('Forgot your password?')
    }

    visit() {
        cy.visit('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index')
    }

    login(username = '', password = '') {
        if (username) this.elements.usernameInput().type(username)
        if (password) this.elements.passwordInput().type(password)
        this.elements.loginButton().click()
    }

    getErrorMessage() {
        return this.elements.errorMessage()
    }

    getRequiredMessage() {
        return this.elements.requiredMessage()
    }

    getForgotPassword() {
        return this.elements.forgotPassword()
    }

    getPasswordField() {
        return this.elements.passwordInput()
    }
}
export default LoginPage