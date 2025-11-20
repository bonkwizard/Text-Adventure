def validEntry(entry, options):
  ##---## Checks if entry is a digit ##---##
  if entry.isdigit():
    ##---## Checks if entry is a valid option ##---##
    if int(entry) <= options:
      return True
    else:
       return False
  else:
    return False