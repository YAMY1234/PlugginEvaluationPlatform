from flask import Flask, render_template, request, send_file
from flask_socketio import SocketIO, send
import io


'''
跟踪技术列表
路径	跟踪技术	说明
/cookies	Cookies	使用Cookies进行用户跟踪
/localstorage	LocalStorage	使用LocalStorage存储用户信息
/sessionstorage	SessionStorage	使用SessionStorage存储会话信息
/pixel	像素追踪	通过一个隐藏的图像跟踪用户
/http-header	HTTP头部信息跟踪	利用HTTP请求的头部信息进行跟踪
/canvas-fingerprint	Canvas指纹识别	使用Canvas生成并跟踪用户的设备指纹
/web-beacons	网络信标	通过Web Beacons进行用户行为跟踪
/user-agent	用户代理字符串	分析用户代理字符串来收集设备和浏览器信息
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cookies')
def cookies():
    return render_template('cookies.html')

@app.route('/localstorage')
def localstorage():
    return render_template('localstorage.html')

# 添加更多的路由和对应的方法...
@app.route('/sessionstorage')
def sessionstorage():
    return render_template('sessionstorage.html')

@app.route('/pixel')
def pixel():
    return render_template('pixel.html')

@app.route('/http-header')
def http_header():
    user_agent = request.headers.get('User-Agent')
    accept_language = request.headers.get('Accept-Language')
    # 这里只是示例，实际应用中可以根据需要记录更多信息
    print(f"User-Agent: {user_agent}, Accept-Language: {accept_language}")
    return render_template('http-header.html')

@app.route('/canvas-fingerprint')
def canvas_fingerprint():
    return render_template('canvas-fingerprint.html')

@app.route('/web-beacons')
def web_beacons():
    return render_template('web-beacons.html')

@app.route('/user-agent')
def user_agent():
    user_agent = request.headers.get('User-Agent')
    # 这里可以进行更深入的用户代理字符串分析，此处仅作打印展示
    print(f"User-Agent: {user_agent}")
    return render_template('user-agent.html')


@app.route('/track')
def track():
    # 记录访问者信息，例如IP地址和User-Agent
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    print(f"Tracked IP: {user_ip}, User-Agent: {user_agent}")

    # 返回一个1x1像素的透明GIF图片
    gif_bytes = b'GIF89a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x01\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02L\x01\x00;'
    return send_file(io.BytesIO(gif_bytes), mimetype='image/gif')

#Test
# @socketio.on('message')
# def handle_message(msg):
#     print('Received message:', msg)
#     send(msg, broadcast=True)
    
# @app.route('/websocket')
# def websocket():
#     return render_template('websocket.html')

if __name__ == '__main__':
    app.run(debug=True)
    # socketio.run(app, debug=True)
