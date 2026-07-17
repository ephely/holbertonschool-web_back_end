const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', function () {
  it('should return 6 when adding 1.4 and 4.5', function () {
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  });
  it('should return -4 when subtracting 1.4 to 4.5', function () {
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
  });
  it('should return 0.2 when dividing 1.4 by 4.5', function () {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
  });
  it('should return an Error when dividing 1.4 by 0', function () {
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
  });
});
