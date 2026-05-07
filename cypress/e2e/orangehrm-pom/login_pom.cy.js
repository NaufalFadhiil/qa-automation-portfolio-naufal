import LoginPage from '../../support/PageObjects/loginPage'
import DashboardPage from '../../support/PageObjects/Dashboard'

describe('OrangeHRM Login with POM', () => {
    
    const loginPage = new LoginPage()
    const dashboardPage = new DashboardPage()

    beforeEach(() => {
        loginPage.visit()
    })

    it('TC_LOGIN_001 - Login dengan kredensial valid', () => {
        cy.intercept('GET', '**/time-at-work**').as('timeAtWork')

        loginPage.login('Admin', 'admin123')
        dashboardPage.verifyDashboard()

        cy.wait('@timeAtWork').its('response.statusCode').should('eq', 200)
    })

    it('TC_LOGIN_002 - Login dengan password salah', () => {
        loginPage.login('Admin', 'salah123')
        
        loginPage.getErrorMessage().should('be.visible')

        cy.url().should('include', '/auth/login')
    })

    it('TC_LOGIN_003 - Login dengan username salah', () => {
        loginPage.login('Salah', 'admin123')
        
        loginPage.getErrorMessage().should('be.visible')

        cy.url().should('include', '/auth/login')
    })

    it('TC_LOGIN_004 - Login tanpa username', () => {
        loginPage.login('', 'admin123')
        
        loginPage.getRequiredMessage().should('be.visible')
    })

    it('TC_LOGIN_005 - Login tanpa password', () => {
        loginPage.login('Admin', '')

        loginPage.getRequiredMessage().should('be.visible')
    })

    it('TC_LOGIN_006 - Login tanpa input apapun', () => {
        loginPage.login('', '')

        loginPage.getRequiredMessage().should('be.visible')
    })

    it('TC_LOGIN_007 - Password harus tersembunyi', () => {
        loginPage.getPasswordField().should('have.attr', 'type', 'password')
    })

    it('TC_LOGIN_008 - Navigasi ke halaman Forgot Forgot Password', () => {
        loginPage.getForgotPassword().click()
        
        cy.url().should('include', 'requestPasswordResetCode')
    })
})