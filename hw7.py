from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

application = Flask(__name__)

application.config['MYSQL_HOST'] = 'localhost'
application.config['MYSQL_USER'] = 'root'
application.config['MYSQL_PASSWORD'] = ''
application.config['MYSQL_DB'] = 'hw7'
application.config['MYSQL_USER'] = 'root'
mysql = MySQL(application)


@application.route('/hw7', methods=['POST'])
def hw7():
    args = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute('SELECT AVG(comm_rate) AS comm_rate_avg, ' +
                'AVG(ind_rate) AS ind_rate_avg, ' +
                'AVG(res_rate) AS res_rate_avg ' +
                'FROM hw7 WHERE state = ' + args['state'] +
                ' AND service_type = ' + args['service_type'])
    rv = cur.ferchall()

    return jsonify({'status': 'OK',
                    'comm_rate_avg': rv.comm_rate_avg,
                    'ind_rate_avg': rv.ind_rate_avg,
                    'res_rate_avg': rv.res_rate_avg})


if __name__ == '__main__':
    application.run(host='0.0.0.0')
