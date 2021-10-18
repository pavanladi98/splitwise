from flask import Flask, request, abort, jsonify, make_response
from splitwise import ExpenseService
from splitwise.exceptions import *
from splitwise.adapter import adapt_user, adapt_expense
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


@app.route('/isalive', methods=['GET'])
@app.route('/api', methods=['GET'])
def isalive():
    """isalive url"""
    return ("SplitWise API - I'm Alive"
            "<br/>Maintainer: <a href='mailto:pavanladi98@gmail.com'>Pavan Kalyan Ladi</a><br/>")


@app.route('/api/v1/user/_create', methods=['POST'])
def create_user():
    """Create User"""
    request_json = request.json
    try:

        user = adapt_user(request_json)
        ExpenseService.create_user(user)
        return jsonify({'status': 'SUCCESS', 'message': f'User is created by id: {user.id}'})
    except HTTPException:
        raise
    except InvalidUserException as err:
        response = jsonify(
            {'status': 'INVALID_USER', 'message': "".join(err.args)})
        return abort(make_response(response, 400))
    except UserAlreadyExistsException as err:
        response = jsonify({'status': 'ALREADY_EXISTS',
                           'message': "".join(err.args)})
        return abort(make_response(response, 400))
    except Exception as err:
        error_response = jsonify(
            {'status': 'UNKNOWN_ERROR', 'message': err.args})
        return abort(make_response(error_response, 500))


@app.route('/api/v1/expense/_create', methods=['POST'])
def create_expense():
    """Create Expense"""
    request_json = request.json
    try:
        expense = adapt_expense(request_json)
        ExpenseService.create_expense(expense)
        return jsonify({'status': 'SUCCESS', 'message': f'Expense is created successfully'})
    except HTTPException:
        raise
    except InvalidUserException as err:
        response = jsonify(
            {'status': 'INVALID_USER', 'message': "".join(err.args)})
        return abort(make_response(response, 400))
    except InvalidExpenseException as err:
        response = jsonify({'status': 'INVALID_EXPENSE',
                           'message': "".join(err.args)})
        return abort(make_response(response, 400))
    except Exception as err:
        error_response = jsonify(
            {'status': 'UNKNOWN_ERROR', 'message': err.args})
        return abort(make_response(error_response, 500))


@app.route('/api/v1/user/_balancesheet', methods=['GET'])
def get_user_balance_sheet():
    """Get Balancesheet for user"""
    request_args = request.args
    try:
        balance_sheet = ExpenseService.get_balance_sheet(
            int(request_args.get('id')))
        return jsonify({'status': 'SUCCESS', 'balance_sheet': balance_sheet})
    except HTTPException:
        raise
    except InvalidUserException as err:
        response = jsonify(
            {'status': 'INVALID_USER', 'message': "".join(err.args)})
        return abort(make_response(response, 400))
    except Exception as err:
        error_response = jsonify(
            {'status': 'UNKNOWN_ERROR', 'message': err.args})
        return abort(make_response(error_response, 500))


@app.route('/api/v1/user/_settle', methods=['GET'])
def settle_balance():
    """Settle balance"""
    request_args = request.args
    try:
        from_id = request_args.get('from_id')
        to_id = request_args.get('to_id')
        ExpenseService.settle_balance(int(from_id), int(to_id))
        return jsonify({'status': 'SUCCESS', 'message': f'Balance settled up between {from_id} and {to_id}'})
    except HTTPException:
        raise
    except InvalidUserException as err:
        response = jsonify(
            {'status': 'INVALID_USER', 'message': "".join(err.args)})
        return abort(make_response(response, 400))
    except Exception as err:
        error_response = jsonify(
            {'status': 'UNKNOWN_ERROR', 'message': err.args})
        return abort(make_response(error_response, 500))


if __name__ == '__main__':
    app.run('0.0.0.0', 3000)
