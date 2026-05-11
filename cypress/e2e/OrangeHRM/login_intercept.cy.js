/// <reference types="cypress" />

describe('OrangeHRM Login with Intercept', () => {

  beforeEach(() => {
    cy.visit('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
  })

  // TC_LOGIN_001
  it('TC_LOGIN_001 - Login dengan kredensial valid', () => {
    cy.intercept('GET', '**/time-at-work**').as('timeAtWork')

    cy.get('input[name="username"]').type('Admin')
    cy.get('input[name="password"]').type('admin123')
    cy.get('button[type="submit"]').click()

    cy.wait('@timeAtWork').its('response.statusCode').should('eq', 200)
    cy.url().should('include', '/dashboard')
  })

  // TC_LOGIN_002
  it('TC_LOGIN_002 - Login dengan password salah', () => {
    cy.get('input[name="username"]').type('Admin')
    cy.get('input[name="password"]').type('salah123')
    cy.get('button[type="submit"]').click()

    cy.contains('Invalid credentials').should('be.visible')
    cy.url().should('include', '/auth/login')
  })

  // TC_LOGIN_003
  it('TC_LOGIN_003 - Login dengan username salah', () => {
    cy.get('input[name="username"]').type('Salah')
    cy.get('input[name="password"]').type('admin123')
    cy.get('button[type="submit"]').click()

    cy.contains('Invalid credentials').should('be.visible')
  })

  // TC_LOGIN_004
  it('TC_LOGIN_004 - Login tanpa username', () => {
    cy.get('input[name="password"]').type('admin123')
    cy.get('button[type="submit"]').click()

    cy.contains('Required').should('be.visible')
  })

  // TC_LOGIN_005
  it('TC_LOGIN_005 - Login tanpa password', () => {
    cy.get('input[name="username"]').type('Admin')
    cy.get('button[type="submit"]').click()

    cy.contains('Required').should('be.visible')
  })

  // TC_LOGIN_006
  it('TC_LOGIN_006 - Login tanpa input apapun', () => {
    cy.get('button[type="submit"]').click()

    cy.contains('Required').should('be.visible')
  })

  // TC_LOGIN_007
  it('TC_LOGIN_007 - Password harus tersembunyi', () => {
    cy.get('input[name="password"]').should('have.attr', 'type', 'password')
  })

  // TC_LOGIN_008
  it('TC_LOGIN_008 - Navigasi ke halaman Forgot Password', () => {
    cy.contains('Forgot your password?').click()
    
    cy.url().should('include', 'requestPasswordResetCode')
  })

})