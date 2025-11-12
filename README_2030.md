AutomationSuite_2030_Proof_FullSystem - README

What's inside:
- core/predictive_optimizer.py : Predictive earnings reallocator
- core/auto_repair_engine.py : Auto-repair diagnostics and safe fixes
- core/ai_runtime_manager.py : Health checks and restart hooks
- interface/telegram_notifier.py : Telegram notifications
- interface/web_dashboard.html : Static demo dashboard
- autorun_diagnostics.py : One-command diagnostics & report (creates autorun_diagnostics.txt)
- launch.bat : Windows helper to run diagnostics

How to run:
1. Extract the zip.
2. (Optional) Set environment variables in your shell or .env:
   - TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
   - AUTO_REPAIR=true  (to enable actual fixes)
3. Run diagnostics:
   python autorun_diagnostics.py
4. Open autorun_diagnostics.txt to view the report.

Security:
- This bundle is safe for dry-run. Auto-fixes require enabling AUTO_REPAIR and network access.
