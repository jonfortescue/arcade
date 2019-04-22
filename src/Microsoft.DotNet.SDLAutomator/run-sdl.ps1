Param(
  [string] $Repository,
  [string] $SourcesDirectory,
  [string] $DncengPat,
  [string[]] $ToolsList,
  [bool] $UpdateBaseline,
)

foreach ($tool in $ToolsList) {
  guardian run --tool $tool --baseline mainbaseline --update-baseline $UpdateBaseline
}

if ($UpdateBaseline) {
  Invoke-Expression "push-gdn.ps1 -Repository $Repository -SourcesDirectory $SourcesDirectory -GdnFolder $SourcesDirectory/.gdn -DncengPat $DncengPat -PushReason `"Update baseline`""
}