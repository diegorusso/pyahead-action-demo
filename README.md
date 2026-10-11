# pyahead-action-demo

A deliberately dated Python project that shows the
[PyAhead](https://github.com/diegorusso/pyahead) GitHub Action at work.

The workflow in `.github/workflows/pyahead.yml` scans `src/` for CPython
deprecations and removals between the project's floor (`requires-python =
">=3.9"`) and the newest Python PyAhead knows, and uploads the findings to
this repository's **Security → Code scanning** tab:

```yaml
- uses: diegorusso/pyahead@v0.6.0
  with:
    fail-on: never
```

The code contains, on purpose:

| file | API | change |
| --- | --- | --- |
| `src/legacyapp/web.py` | `cgi` | removed in Python 3.13 |
| `src/legacyapp/clock.py` | `datetime.utcnow` | deprecated in 3.12 |
| `src/legacyapp/loop.py` | `asyncio.get_event_loop_policy` | deprecated in 3.14, removed in 3.16 |
| `src/legacyapp/compat.py` | `collections.Mapping` fallback | guarded; PyAhead reports nothing |

Run the workflow by hand with `fail-on: breaking` to see the job fail on the
`cgi` import while the findings still reach code scanning.
