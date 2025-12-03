from wagtail import hooks
from django.urls import path, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from wagtail.admin.menu import MenuItem
from .models import AuditRecord, WCAGIssue
from .services import run_pa11y_audit


@hooks.register('register_admin_urls')
def register_audit_urls():
    return [
        path('run-audit/', run_audit_view, name='run_audit'),
        path('audit-history/', audit_history_view, name='audit_history'),
        path('audit-detail/<int:audit_id>/', audit_detail_view, name='audit_detail'),
    ]


@hooks.register('register_admin_menu_item')
def register_audit_menu_item():
    return MenuItem('Run Audit', reverse('run_audit'), icon_name='doc-full-inverse', order=10000)


@hooks.register('register_admin_menu_item')
def register_history_menu_item():
    return MenuItem('Audit History', reverse('audit_history'), icon_name='list-ul', order=10001)


def run_audit_view(request):
    if request.method == 'POST':
        page_url = request.POST.get('page_url')
        page_name = request.POST.get('page_name')
        notes = request.POST.get('notes', '')
        if page_url and page_name:
            audit = run_pa11y_audit(page_url, page_name, notes)
            messages.success(request, f'Audit completed! Found {audit.issues_found} issues.')
            return redirect('audit_detail', audit_id=audit.id)
    return render(request, 'audit/run_audit.html')


def audit_history_view(request):
    audits = AuditRecord.objects.all()
    context = {
        'audits': audits,
        'total_audits': audits.count(),
        'total_issues': sum(a.issues_found for a in audits)
    }
    return render(request, 'audit/audit_history.html', context)


def audit_detail_view(request, audit_id):
    audit = get_object_or_404(AuditRecord, id=audit_id)
    issues = audit.wcag_issues.all()
    context = {
        'audit': audit,
        'issues': issues
    }
    return render(request, 'audit/audit_detail.html', context)
