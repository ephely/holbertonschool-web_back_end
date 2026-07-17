const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', function () {
  it('should return 6 when adding 1.4 and 4.5', function () {
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
  });
  it('should return -4 when subtracting 1.4 to 4.5', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
  });
  it('should return 0.2 when dividing 1.4 by 4.5', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
  });
  it('should return an Error when dividing 1.4 by 0', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });
});
