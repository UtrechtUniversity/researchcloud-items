# -*- mode: ruby -*- vim: set syntax=ruby
# frozen_string_literal: true

has_app_changes = !git.modified_files.grep(/(files|defaults|tasks|handlers|meta|templates)/).empty?

if git.commits.any? { |c| c.message =~ /^Merge branch/ }
  fail('Please rebase to get rid of the merge commits in this PR!')
  message "For more information, please see [man git-rebase](https://git-scm.com/docs/git-rebase)."
end

if !git.modified_files.include?("CHANGELOG.md") && has_app_changes
  fail("Please include a CHANGELOG entry. \nYou can find it at [CHANGELOG.md](https://github.com/hetznercloud/ansible-role-ipxe-ca/blob/main/CHANGELOG.md).")
  message "Note, we use [changelogger](https://github.com/MarkusFreitag/changelogger) as changelog tooling."
end
