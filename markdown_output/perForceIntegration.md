---
title: "Perforce Integration"
category: "General"
source_file: "perForceIntegration.html"
doc_type: "manual"
---

# Perforce Integration

For more information on **Perforce** , visit www.perforce.com.

## Setting up Perforce

Follow the setup process described in the Version Control documentation. See Perforce documentation if you encounter any problems.

**Note** : If your Perforce workspace has multi-factor authentication enabled you will first need to login through the command line using _p4 login2_ or by using a visual client like P4V to be able to login in the Unity Editor as well.

## Integration through the CLI

When you connect Perforce through the command line interface, the provider is enabled immediately but only becomes active after `Provider.UpdateSettings()` completes its asynchronous update.

**Note** : If your workflow requires the provider to be active immediately, call `Provider.UpdateSettings().Wait()` before you check the provider state.

## Working offline with Perforce

Only use this if you know how to work offline in Perforce without a Sandbox. Refer to the Perforce documentation for further information.

## Troubleshooting

If Unity cannot commit your changes to Perforce (for example, if the server is down, or you experience licensing issues), your changes are stored in a separate changeset. If the console doesn’t list any info about the issue, you can use the P4V client for Perforce to submit this changeset to see the exact error message.

You cannot submit changes if you are sharing a workspace with another user. A workspace should be dedicated to one user only.

## Automatic revert of unchanged files on submit

It’s possible to configure Perforce to revert unchanged files on submit. To do this in P4V, select **Connection** > **Edit Current Workspace** , view the **Advanced** tab and set the value of **On submit** to **Revert unchanged files**.