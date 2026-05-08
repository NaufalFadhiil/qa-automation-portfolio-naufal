import ForgotPasswordPage from '../../support/PageObjects/forgotPasswordPage'
import forgotPasswordData from '../../fixtures/forgot_PasswordData.json'

describe('OrangeHRM Forgot Password Feature', () => {

    const forgotPasswordPage = new ForgotPasswordPage()

    beforeEach(() => {
        forgotPasswordPage.visitForgotPassword()
    })

    it('TC_FP_001 - Navigate Forgot Password Page', () => {

        cy.url().should('include', 'requestPasswordResetCode')

    })

    it('TC_FP_002 - Submit Empty Username', () => {

        forgotPasswordPage.clickResetButton()

        forgotPasswordPage
            .getRequiredMessage()
            .should('be.visible')

    })

    it('TC_FP_003 - Click Cancel Button', () => {

        forgotPasswordPage.clickCancelButton()

        cy.url().should('include', 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    })

    it('TC_FP_004 - Submit Valid Username', () => {

        forgotPasswordPage.inputUsername(forgotPasswordData.validUsername)

        forgotPasswordPage.clickResetButton()

        forgotPasswordPage
            .getSuccessMessage()
            .should('be.visible')

        cy.contains(forgotPasswordData.successMessage)
            .should('be.visible')

    })

})