import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.root = Path(folder.name)
        self.fixture = json.loads((ROOT / 'data/workbench.json').read_text())
        self.save()

    def save(self):
        (self.root / 'workbench.json').write_text(json.dumps(self.fixture))

    def run_action(self, action, key=None, succeeds=True):
        args = [sys.executable, '-m', 'app', action, '--data', str(self.root),
                '--ledger', str(self.root / 'receipts.sqlite3')]
        if key is not None:
            args.extend(['--key', key])
        proc = subprocess.run(args, cwd=ROOT, text=True, capture_output=True, timeout=5)
        if succeeds:
            self.assertEqual(proc.returncode, 0, proc.stderr)
            return json.loads(proc.stdout)
        self.assertEqual(proc.returncode, 2, proc.stderr)
        return proc.stderr

    def test_station_dispatch_and_withdrawal(self):
        before = self.run_action('dispatch')
        self.assertEqual(before['station_opens'], {'coast': 2, 'harbor': 2})
        self.fixture['editions'][1]['state'] = 'withdrawn'
        self.save()
        self.assertNotIn('s1-en', self.run_action('edition'))
        self.assertEqual(self.run_action('traffic')['station_opens'], {'harbor': 2})
        self.assertEqual(self.run_action('archive', '2026-W24'), before)
        self.assertIn('不同内容', self.run_action('dispatch', succeeds=False))
