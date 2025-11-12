"""Autorun Diagnostics - single command verification for core system"""
import os, time, json, logging, subprocess
from core.predictive_optimizer import recommend_reallocation
from core.auto_repair_engine import run_diagnostics_and_fix
from core.ai_runtime_manager import health_check
from interface.telegram_notifier import send_message

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('autorun')

REPORT_PATH = 'autorun_diagnostics.txt'

def run_all_checks():
    report = {'timestamp': time.time(), 'checks': []}
    # health check
    health = health_check()
    report['checks'].append({'health': health})
    # predictive optimizer sample run
    sample = {'o1':[10,12,11,13],'o2':[5,6,4,3],'o3':[20,22,25,30]}
    rec = recommend_reallocation(sample, 200.0)
    report['checks'].append({'predictive_sample': rec})
    # simulate log lines for auto repair
    sample_logs = ['ModuleNotFoundError: No module named \"foobar\"', 'Connection refused to db:5432']
    repairs = run_diagnostics_and_fix(sample_logs)
    report['checks'].append({'repairs': repairs})
    # write report
    with open(REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write(json.dumps(report, indent=2))
    logger.info('Diagnostics written to %s', REPORT_PATH)
    try:
        send_message('Autorun Diagnostics', 'Diagnostics completed. Check autorun_diagnostics.txt')
    except Exception:
        pass
    return report

if __name__ == '__main__':
    r = run_all_checks()
    print('Diagnostics complete. See autorun_diagnostics.txt')
