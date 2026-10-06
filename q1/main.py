import json
import os
result = {'total': 0, 'by_level': {}, 'by_user': {}, 'last_error': None}
def analyze_log(filepath):
    if not os.path.exists(filepath):
        return result
    try:
        with open(filepath,'r',encoding='utf-8')as f:
            for line in f:
                line=line.strip()
                if not line:
                    continue
                try:
                    log_data=json.loads(line)
                    result['total'] += 1
                    level=log_data["level"]
                    user=log_data["user"]
                    message=log_data["message"]
                    if level in result['by_level']:
                        result['by_level'][level]=result['by_level'][level]+1
                    else:
                        result['by_level'][level]=1
                    if user in result['by_user']:
                        result['by_user'][user]=result['by_user'][user]+1
                    else:
                        result['by_user'][user]=1
                    if level == "ERROR":
                        result['last_error']=message
                except json.JSONDecodeError:
                    continue
    except Exception:
        pass
    return result
