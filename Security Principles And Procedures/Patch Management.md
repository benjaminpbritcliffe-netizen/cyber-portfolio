
# Patch Management

An effective patch management strategy requires patch management software
to be configured based on the risks associated with each system and its applications.
Mission-critical systems must be treated differently,
than less critical ones to support availability requirements.
Desktops are often patched as quickly as possible after a brief testing phase.

Testing consists of:

verifying the functionality and compatibility of a patch before deployment,
as well as any potential risks it poses to the system.

After the tests have been conducted,
the patch can be implemented on the computer or device.

In the event of a problem,
the patch can be rolled back to avoid further disruption to the system.

Finally,
the patch must be validated to ensure it is effective and secure before deployment.

## Considerations

Patch Management Considerations
Important patch management considerations include the following:

An individual or task-specific team responsible
for reviewing vendor-supplied newsletters and security patch bulletins.

Mechanisms to patch operating systems and all applications running on them,
regardless of application vendor.

Patch management principles that incorporate cloud resources.

Assigning updates into urgent, important, and non-critical categories.

A patch test environment
where urgent and important patches can be:
installed, tested, and analyzed before deployment into production.

Detailed logging
designed to support monitoring and troubleshooting of patch deployment activities.

A method to evaluate firmware updates before deployment.

Immediate push delivery of critical security patches.

A routine schedule for the rollout of non-critical patches.

## Patch Testing

Patch testing aims to determine whether:
a software patch creates problems with the organization's unique mix of:
hardware,
software,
and configuration settings.

Patch testing should primarily involve testing a patch on a single isolated system,
to determine whether a patch causes problems,
such as software crashes or system instability.

Additionally,
testing should validate those issues addressed by the software patchwork as expected.
For example, a patch successfully removes a vulnerability.

A common way to test a patch is by setting up a non-production environment -
hosting like-for-like mission-critical applications,
including enterprise applications and networking systems (where available).

Doing this allows patches to be deployed by infrastructure teams,
validated by software support staff,
and assessed by security teams before deployment into the production environment.

Additionally,
vulnerability scans should verify that patches only resolve vulnerabilities,
and do not introduce any new ones!

## Patch Management Lifecycle

Testing (Sandbox)

Verification (Technical Check)

Implementation (Production Rollout)

Validation (Functional Check)

Rollback (Triggered only if Step 4 fails)
