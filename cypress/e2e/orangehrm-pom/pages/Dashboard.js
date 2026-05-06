class DashboardPage {

    verifyDashboard() {
        cy.url().should('include', '/dashboard')
    }
}

export default DashboardPage