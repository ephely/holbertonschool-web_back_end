import Currency from './3-currency';

export default class Pricing {
    constructor(amount, currency) {
        if (typeof amount !== 'number') {
            throw new TypeError('Amount must be a number');
        }
        if (!(currency instanceof Currency)) {
            throw new TypeError('Currency must be an instance of currency');
        }
        
        this._amount = amount;
        this._currency = currency;
    }
  
    get amount() {
        return this._amount;
    }
    
    set amount(value) {
        if (typeof value !== 'number') {
            throw new TypeError('Amount must be a number');
        }
        this._amount = value;
    }
    
    get currency() {
        return this._currency;
    }
    
    set currency(value) {
        if (!(value instanceof Currency)) {
            throw new TypeError('Currency must be an instance of Currency');
        }
        this._currency = value;
    }

    displayFullPrice() {
        return `${this._amount} ${this._currency.name} (${this._currency.code})`;
    }

    static convertPrice(amount, conversionRate) {
        if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
            throw new TypeError('Both amount and conversionRate must be a number');
        }
        return amount * conversionRate;
    }
}