/// <reference types="cypress" />

describe('Platzi Categories - API Automation', () => {
    it('TC_API_001 - Get all categories', () => {
        cy.request('GET', 'https://api.escuelajs.co/api/v1/categories')
            .then((response) => {
            expect(response.status).to.eq(200)
            expect(response.body).to.be.an('array')
            expect(response.body).to.not.be.null
        })
    })

    it('TC_API_002 - Get a category by ID', () => {
        cy.request('GET', 'https://api.escuelajs.co/api/v1/categories/1')
            .then((response) => {
            expect(response.status).to.eq(200)
            expect(response.body).to.be.an('object')
            expect(response.body).to.not.be.null
        })
    })

    it('TC_API_003 - Get category by ID (invalid ID)', () => {
        cy.request({
            method: 'GET',
            url: 'https://api.escuelajs.co/api/v1/categories/9999',
            failOnStatusCode: false
        }).then((response) => {
            expect(response.status).to.eq(400) 
            expect(response.body).to.be.an('object')
        })
    })

    it('TC_API_004 - Post create category', () => {
        cy.request({
            method: 'POST',
            url: 'https://api.escuelajs.co/api/v1/categories',
            body: {
                "name": "New category - Shoes",
                "image": "https://placeimg.com/640/480/any"
            }
        }).then((response) => {
            expect(response.status).to.eq(201)
            expect(response.body).to.have.property('id')
            expect(response.body.name).to.eq('New category - Shoes')
            expect(response.body.image).to.eq('https://placeimg.com/640/480/any')
        })
    })

    it('TC_API_005 - Update category by ID', () => {
        cy.request({
            method: 'PUT',
            url: 'https://api.escuelajs.co/api/v1/categories/90',
            body: {
            name: 'Updated Category - Shoes'
            }
        }).then((response) => {
            expect(response.status).to.eq(200)
            expect(response.body.name).to.eq('Updated Category - Shoes')
        })
    })

    it('TC_API_006 - Update category by ID (invalid ID)', () => {
        cy.request({
            method: 'PUT',
            url: 'https://api.escuelajs.co/api/v1/categories/9999',
            failOnStatusCode: false
        }).then((response) => {
            expect(response.status).to.eq(400) 
        })
    })

    it('TC_API_007 - Delete category', () => {
        cy.request({
            method: 'DELETE',
            url: 'https://api.escuelajs.co/api/v1/categories/4',
            failOnStatusCode: false
        }).then((response) => {
            expect(response.status).to.eq(200)            
            expect(response.body).to.not.be.null
        })
    })
})