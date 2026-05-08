import LoginPage from '../../support/PageObjects/loginPage'
import DashboardPage from '../../support/PageObjects/Dashboard'
import DirectoryPage from '../../support/PageObjects/directoryPage'
import loginData from '../../fixtures/loginData.json'
import directoryData from '../../fixtures/directoryData.json'

describe('OrangeHRM Directory Feature', () => {

    const loginPage = new LoginPage()
    const dashboardPage = new DashboardPage()
    const directoryPage = new DirectoryPage()

    beforeEach(() => {

        loginPage.visit()

        loginPage.login(
            loginData.validUsername,
            loginData.validPassword
        )

        dashboardPage.verifyDashboard()

        directoryPage.clickDirectoryMenu()

    })

    it('TC_DIR_001 - Navigate to Directory Page', () => {

        cy.url().should('include', '/directory')

    })

    it('TC_DIR_002 - Search Valid Employee', () => {

        cy.intercept(
            'GET',
            '**/api/v2/directory/employees*'
        ).as('searchEmployee')

        directoryPage.inputEmployeeName(directoryData.validEmployeeName)

        directoryPage.clickSearchButton()

        cy.wait('@searchEmployee')
            .its('response.statusCode')
            .should('eq', 200)

        directoryPage
            .getEmployeeCard()
            .should('be.visible')

    })

    it('TC_DIR_003 - Search Invalid Employee', () => {

        cy.intercept(
            'GET',
            '**/api/v2/directory/employees*'
        ).as('invalidSearch')

        directoryPage.inputEmployeeName(directoryData.invalidEmployeeName)

        directoryPage.clickSearchButton()

        cy.wait('@invalidSearch')
            .its('response.statusCode')
            .should('eq', 200)

        directoryPage
            .getInvalidText()
            .should('be.visible')

    })

    it('TC_DIR_004 - Reset Employee Search Field', () => {
        cy.intercept(
            'GET',
            '**/api/v2/directory/employees*'
        ).as('resetSearch')

        directoryPage.clickResetButton()

        cy.wait('@resetSearch')
            .its('response.statusCode')
            .should('eq', 200)
    })

})