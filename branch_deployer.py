#!/usr/bin/env python3
"""Deploy branch to staging environment"""
import argparse
def main():
 p=argparse.ArgumentParser(description="Deploy branch to staging environment")
 p.add_argument("--version",action="store_true")
 args=p.parse_args()
 if args.version:print("branch-deployer v0.1.0");return
 print(f"[12:00] branch-deployer ready")
if __name__=="__main__":main()
