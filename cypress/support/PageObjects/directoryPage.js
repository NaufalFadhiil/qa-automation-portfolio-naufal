class DirectoryPage {

    elements = {

        directoryMenu: () => cy.contains('Directory'),

        employeeNameInput: () => cy.get("input[placeholder='Type for hints...']"),

        searchButton: () => cy.get("button[type='submit']"),

        resetButton: () => cy.get("button[type='reset']"),

        noRecordText: () => cy.contains('No Records Found'),

        employeeCard: () => cy.get('.orangehrm-directory-card'),

        invalidText: () => cy.contains('Invalid')
    }

    clickDirectoryMenu() {
        this.elements.directoryMenu().click()
    }

    inputEmployeeName(employeeName) {
        this.elements.employeeNameInput().type(employeeName)
    }

    clickSearchButton() {
        this.elements.searchButton().click()
    }

    clickResetButton() {
        this.elements.resetButton().click()
    }

    getNoRecordText() {
        return this.elements.noRecordText()
    }

    getEmployeeCard() {
        return this.elements.employeeCard()
    }

    getInvalidText() {
        return this.elements.invalidText()
    }
}

export default DirectoryPage