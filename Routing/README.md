If you want to save only 'warning' and 'error' (and not 'info') log messages to a file, just open a console and type:
    python receive_logs_direct.py warning error > logs_from_rabbit.log
If you'd like to see all the log messages on your screen, open a new terminal and do:
    python receive_logs_direct.py info warning error
        # => [*] Waiting for logs. To exit press CTRL+C
And, for example, to emit an error log message just type:
    python emit_log_direct.py error "Run. Run. Or it will explode."
        # => [x] Sent 'error':'Run. Run. Or it will explode.'