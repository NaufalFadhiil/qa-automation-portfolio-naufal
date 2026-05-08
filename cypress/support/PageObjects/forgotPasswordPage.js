class ForgotPasswordPage {

    elements = {
        usernameInput: () => cy.get('input[name="username"]'),
        cancelButton: () => cy.contains('button', 'Cancel').first(),
        resetButton: () => cy.contains('button', 'Reset Password').first(),
        requiredMessage: () => cy.contains('Required'),
        successMessage: () => cy.contains('Reset Password link sent successfully')
    }

    visitForgotPassword() {
        cy.visit('https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode')
    }

    inputUsername(username) {
        this.elements.usernameInput().type(username)
    }

    clickResetButton() {
        this.elements.resetButton().click()
    }

    clickCancelButton() {
        this.elements.cancelButton().click()
    }

    getRequiredMessage() {
        return this.elements.requiredMessage()
    }

    getSuccessMessage() {
        return this.elements.successMessage()
    }
}

export default ForgotPasswordPage