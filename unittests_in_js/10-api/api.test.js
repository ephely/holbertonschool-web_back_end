const request = require('request');
const { expect } = require('chai');

describe('Index page', function () {
  const url = 'http://localhost:7865/';

  it('Correct status code?', function (done) {
    request(url, function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct result?', function (done) {
    request(url, function (error, response, body) {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Cart page', function () {
  it('Correct status code when :id is a number?', function (done) {
    request('http://localhost:7865/cart/12', function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct result when :id is a number?', function (done) {
    request('http://localhost:7865/cart/12', function (error, response, body) {
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('Correct status code when :id is NOT a number (=> 404)?', function (done) {
    request('http://localhost:7865/cart/hello', function (error, response, body) {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});

describe('Available payments page', function () {
  it('Correct status code?', function (done) {
    request('http://localhost:7865/available_payments', function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct payment methods object (deep equality)?', function (done) {
    request('http://localhost:7865/available_payments', function (error, response, body) {
      expect(JSON.parse(body)).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false,
        },
      });
      done();
    });
  });
});

describe('Login page', function () {
  it('Correct status code?', function (done) {
    request.post(
      {
        url: 'http://localhost:7865/login',
        json: true,
        body: { userName: 'Betty' },
      },
      function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        done();
      }
    );
  });

  it('Correct welcome message?', function (done) {
    request.post(
      {
        url: 'http://localhost:7865/login',
        json: true,
        body: { userName: 'Betty' },
      },
      function (error, response, body) {
        expect(body).to.equal('Welcome Betty');
        done();
      }
    );
  });
});
