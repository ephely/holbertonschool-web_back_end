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
